import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.check_connect import check_db_connected, check_db_disconnected
from app.routes.category import categoryrouter
from app.routes.user import user_router
from app.routes.auth import authrouter
from app.routes.product import productrouter
from app.routes.order import orderrrouter
from app.routes.cart import cartrouter
from app.routes.review import reviewrouter
from app.routes.slider import sliderrouter
from app.routes.rajaongkir import rajaongkir_router
from app.routes.midtrans import midtransrouter
from app.core.database import Base, engine
from app.core.cloudinary import my_cloudinary
from app.routes.dashboard import dashboardrouter


app = FastAPI()
my_cloudinary

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def runtimeStartup():
    await check_db_connected()
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
async def runtimestop():
    await check_db_disconnected()


@app.get("/")
def hello():
    return "Hello"


app.include_router(categoryrouter, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(authrouter, prefix="/api")
app.include_router(productrouter, prefix="/api")
app.include_router(cartrouter, prefix="/api")
app.include_router(orderrrouter, prefix="/api")
app.include_router(sliderrouter, prefix="/api")
app.include_router(rajaongkir_router, prefix="/api")
app.include_router(midtransrouter, prefix="/api")
app.include_router(reviewrouter, prefix="/api")
app.include_router(dashboardrouter, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
