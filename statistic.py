from pydantic import BaseModel


class Statistic(BaseModel):
    viewCount: int
    subscriberCount: int
    hiddenSubscriberCount: bool
    videoCount: int
