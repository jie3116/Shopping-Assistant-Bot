from fastapi import APIRouter, Query
from backend.services.product_service import search_product

router = APIRouter(
    tags=["Products"]
)

@router.get("/search")
def search(query: str = Query(..., description="Nama produk")):
    return search_product(query)
