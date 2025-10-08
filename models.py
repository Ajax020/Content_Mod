from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class ModerationRequest(Base):
    __tablename__ = "moderation_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, nullable=False)
    content_type = Column(String, nullable=False)  # text or image
    content_hash = Column(String, nullable=False)
    status = Column(String, default="processed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    result = relationship("ModerationResult", back_populates="request", uselist=False)

class ModerationResult(Base):
    __tablename__ = "moderation_results"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("moderation_requests.id"))
    classification = Column(String, nullable=False)  # toxic/spam/safe/etc
    confidence = Column(Float)
    reasoning = Column(Text)
    llm_response = Column(Text)

    request = relationship("ModerationRequest", back_populates="result")
