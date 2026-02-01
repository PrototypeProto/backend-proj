from src.db.models import Product
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import ProductCreateModel, ProductUpdateModel
from sqlmodel import select, desc
from datetime import date, datetime

'''
    Handles business logic (db access) for the {/products} route
    enforce proper data insertions 
'''

class ProductService:
    async def get_all_products(self, session:AsyncSession):
        statement = select(Product).order_by(desc(Product.date_introduced))

        result = await session.exec(statement)
        return result.all()

    async def get_product(self, product_uid:str, session:AsyncSession):
        statement = select(Product).where(Product.uid == product_uid)

        result = await session.exec(statement)

        product = result.first()

        return product if product is not None else None

    async def create_product(self, product_data:ProductCreateModel, session:AsyncSession) -> Product:
        product_data_dict = product_data.model_dump()
        
        new_product = Product(
            **product_data_dict
        )

        session.add(new_product)

        await session.commit()

        return new_product

    async def update_product(self, product_uid:str, update_data:ProductUpdateModel, session:AsyncSession):
        product_to_update = await self.get_product(product_uid, session)

        if product_to_update is not None:
            update_data_dict = update_data.model_dump()
            update_data_dict["time_modified"] = datetime.now()

            for k, v in update_data_dict.items():
                setattr(product_to_update, k, v)

            await session.commit()

            return product_to_update
        else:
            return None

    async def delete_product(self, product_uid:str, session:AsyncSession) -> bool:
        product_to_delete = await self.get_product(product_uid, session)

        if product_to_delete is not None:
            await session.delete(product_to_delete)

            await session.commit()

            return True
            
        else: 
            return False