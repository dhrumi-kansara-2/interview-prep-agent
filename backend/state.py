from typing import TypedDict, List, Optional
from backend.schemas.models import GapAnalysis, InterviewQuestion, AnswerEvaluation, SessionReport

class AgentState(TypedDict):
    session_id: str
    resume_text: str
    job_description: str
    gap_analysis: Optional[GapAnalysis]
    questions: Optional[List[InterviewQuestion]]
    current_question_index: int
    evaluations: Optional[List[AnswerEvaluation]]
    session_report: Optional[SessionReport]
