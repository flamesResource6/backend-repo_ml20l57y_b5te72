"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List

# Portfolio-related schemas

class Profile(BaseModel):
    """
    Personal profile information for the portfolio
    Collection name: "profile"
    """
    name: str = Field(..., description="Full name")
    title: str = Field(..., description="Professional title")
    bio: str = Field(..., description="Short biography")
    location: Optional[str] = Field(None, description="Location")
    avatar_url: Optional[HttpUrl] = Field(None, description="Profile image URL")
    email: Optional[EmailStr] = Field(None, description="Contact email")
    socials: Optional[dict] = Field(default_factory=dict, description="Map of social links")

class Project(BaseModel):
    """
    Projects showcased in the portfolio
    Collection name: "project"
    """
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Short description")
    tags: List[str] = Field(default_factory=list, description="Tech stack tags")
    image_url: Optional[HttpUrl] = Field(None, description="Cover image URL")
    demo_url: Optional[HttpUrl] = Field(None, description="Live demo URL")
    repo_url: Optional[HttpUrl] = Field(None, description="Source code URL")
    featured: bool = Field(default=True, description="Showcase on homepage")

class Experience(BaseModel):
    """
    Work experience or education timeline
    Collection name: "experience"
    """
    company: str = Field(..., description="Company or institution")
    role: str = Field(..., description="Role or degree")
    start: str = Field(..., description="Start date (e.g., Jan 2022)")
    end: str = Field(..., description="End date or 'Present'")
    summary: Optional[str] = Field(None, description="What you did/learned")

class Skill(BaseModel):
    """
    Skills with optional proficiency
    Collection name: "skill"
    """
    name: str = Field(..., description="Skill name")
    level: Optional[int] = Field(None, ge=1, le=100, description="Proficiency from 1-100")
    group: Optional[str] = Field(None, description="Category e.g. Frontend, Backend")

class Message(BaseModel):
    """
    Contact form submissions
    Collection name: "message"
    """
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    subject: str = Field(..., description="Message subject")
    body: str = Field(..., description="Message body")

# Example legacy schemas retained for reference (not used by portfolio)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
