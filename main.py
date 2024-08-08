from fastapi import FastAPI

from backend.settings import settings

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
    version=settings.project_version,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

# Include all routers
# app.include_router(item.router)
