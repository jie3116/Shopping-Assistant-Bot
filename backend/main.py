from fastapi import FastAPI
from backend.api.user import router as user_router
from backend.api.product import router as product_router

app = FastAPI(title="Shopping Assistant Bot API", description="API for the Shopping Assistant Chatbot.")
app.include_router(user_router, prefix="/users")
app.include_router(product_router, prefix="/products")

@app.get("/")
def root():
    return {"message": "Hello from Shopping Assistant Chatbot!"}


#uvicorn backend.main:app --reload
