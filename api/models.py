from pydantic import (BaseModel, 
                      field_validator,
                      ValidationError,
                      ValidationInfo)


class QuizModel(BaseModel):
    question_count: int

    @field_validator("question_count")
    @classmethod
    def count_must_be_positive(cls, value: int, info: ValidationInfo) -> int:
        if value > 0:
            return value
        else:
            raise ValueError(f"{info.field_name} должно быть положительным"
                             f" числом более 0")

