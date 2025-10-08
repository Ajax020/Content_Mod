from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib
import random

from database import Base, engine, SessionLocal
from models import ModerationRequest, ModerationResult
from schemas import TextModerationRequest, ModerationResponse

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Content Moderator API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/moderate/text", response_model=ModerationResponse)
def moderate_text(request: TextModerationRequest, db: Session = Depends(get_db)):
    """
    1. Takes user's email and content.
    2. Hashes content for tracking.
    3. Uses a dummy AI logic to classify text (simulating GPT).
    4. Saves request + result to the database.
    """

    # Step 1: Create hash of the content
    content_hash = hashlib.sha256(request.content.encode()).hexdigest()

    # Step 2: Simulated AI classification logic
    possible_labels = ["safe", "toxic", "spam", "harassment"]
    classification = random.choice(possible_labels)
    confidence = round(random.uniform(0.75, 0.99), 2)
    reasoning = f"The text was classified as {classification} based on simple keyword analysis."

    # Step 3: Store moderation request
    new_request = ModerationRequest(
        user_email=request.email,
        content_type="text",
        content_hash=content_hash,
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    # Step 4: Store moderation result
    new_result = ModerationResult(
        request_id=new_request.id,
        classification=classification,
        confidence=confidence,
        reasoning=reasoning,
        llm_response=f"Simulated response for: {request.content}"
    )
    db.add(new_result)
    db.commit()

    # Step 5: Return the moderation result
    return ModerationResponse(
        classification=classification,
        confidence=confidence,
        reasoning=reasoning
    )
