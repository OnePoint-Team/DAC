from core.factories import settings
from datetime import datetime, timedelta
from app.data.models import (
    Users,
    User_Groups,
    Groups,
    Service,
    Endpoint,
    Method,
    Permission,

)
from pydantic import parse_obj_as
from uuid import UUID
from fastapi import HTTPException
from fastapi import Header
from core.extensions import log
from sqlalchemy import and_
from app.controllers.controller.schemas import (
    UserSchema,
    UserSchemaDB,
    UserGroupSchema,
    UserGroupSchemaDB,
    GroupSchema,
    GroupSchemaDB,
    ServiceSchema,
    ServiceSchemaDB,
    EndpointSchema,
    EndpointSchemaDB,
    MethodSchema,
    MethodSchemaDB,
    PermissionSchema, 
    PermissionSchemaDB,
    UpdateEndpointSchema,
    UpdatePermissionSchema,
    UpdateUserGroupSchema,
    UpdateUserSchema,
   
)
from core.extensions import db
from starlette.responses import JSONResponse
from http import HTTPStatus
from typing import List
import jwt, json,hashlib


# --------------- CREATE -----------------------

def clean_dict(data : dict) -> dict:
    return {key: val for (key, val) in data.items() if val is not None}

async def create_user(data: UserSchema):
    try:
        async with db.transaction() as ctx:
            await Users.create(**data.dict())
            return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
    except Exception as err:
        log.error(f"Error on create_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def create_group(data: GroupSchema):
    try:
        async with db.transaction() as ctx:
            await Groups.create(**data.dict())
            return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
    except Exception as err:
        log.error(f"Error on create_group function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



async def create_us_gr(data: UserGroupSchema):
    try:
        async with db.transaction() as ctx:
            await User_Groups.create(**data.dict())
            return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
    except Exception as err:
        log.error(f"Error on create_us_gr function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def create_service(data: ServiceSchema):
    try:
        async with db.transaction() as ctx:
            await Service.create(**data.dict())
            return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
    except Exception as err:
        log.error(f"Error on create_service function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



async def create_method(data: MethodSchema):
    try:
        async with db.transaction() as ctx:
            await Method.create(**data.dict())
            return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
    except Exception as err:
        log.error(f"Error on create_method function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)




async def create_permission(data: PermissionSchema):
    try:
        async with db.transaction() as ctx:
            await Permission.create(**data.dict())
            return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
    except Exception as err:
        log.error(f"Error on create_method function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



# --------------- UPDATE -----------------------

async def update_user(data: UpdateUserSchema,id: UUID):
    try:
        async with db.transaction() as ctx:
            user = await Users.query.where(Users.id == id).gino.first()
            if user:
                data =  clean_dict(data.dict())
                await user.update(**data).apply()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)

    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def update_group(data: GroupSchema,id: UUID):
    try:
        async with db.transaction() as ctx:
            group = await Groups.query.where(Groups.id == id).gino.first()
            if group:
                data =  clean_dict(data.dict())
                await group.update(**data).apply()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)

    except Exception as err:
        log.error(f"Error on update_group function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def update_us_gr(data: UpdateUserGroupSchema,id: UUID):
    try:
        async with db.transaction() as ctx:
            group = await User_Groups.query.where(User_Groups.id == id).gino.first()
            if group:
                data =  clean_dict(data.dict())
                await group.update(**data).apply()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)

    except Exception as err:
        log.error(f"Error on update_us_gr function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def update_service(data: ServiceSchema,id: UUID):
    try:
        async with db.transaction() as ctx:
            service = await Service.query.where(Service.id == id).gino.first()
            if service:
                data =  clean_dict(data.dict())
                await service.update(**data).apply()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)

    except Exception as err:
        log.error(f"Error on update_us_gr function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def update_method(data: MethodSchema,id: UUID):
    try:
        async with db.transaction() as ctx:
            method = await Method.query.where(Method.id == id).gino.first()
            if method:
                data =  clean_dict(data.dict())
                await method.update(**data).apply()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)

    except Exception as err:
        log.error(f"Error on update_us_gr function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def update_permission(data: UpdatePermissionSchema,id: UUID):
    try:
        async with db.transaction() as ctx:
            permission = await Permission.query.where(Permission.id == id).gino.first()
            if permission:
                data =  clean_dict(data.dict())
                await permission.update(**data).apply()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)

    except Exception as err:
        log.error(f"Error on update_us_gr function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



# --------------- DELETE -----------------------


async def delete_user(id: UUID):
    try:
        async with db.transaction() as ctx:
            user = await Users.query.where(Users.id == id).gino.first()
            if user:
                await user.delete()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def delete_group(id: UUID):
    try:
        async with db.transaction() as ctx:
            group = await Groups.query.where(Groups.id == id).gino.first()
            if group:
                await group.delete()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def delete_us_gr(id: UUID):
    try:
        async with db.transaction() as ctx:
            group = await User_Groups.query.where(User_Groups.id == id).gino.first()
            if group:
                await group.delete()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def delete_service(id: UUID):
    try:
        async with db.transaction() as ctx:
            service = await Service.query.where(Service.id == id).gino.first()
            if service:
                await service.delete()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



async def delete_method(id: UUID):
    try:
        async with db.transaction() as ctx:
            method = await Method.query.where(Method.id == id).gino.first()
            if method:
                await method.delete()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def delete_permission(id: UUID):
    try:
        async with db.transaction() as ctx:
            permission = await Permission.query.where(Permission.id == id).gino.first()
            if permission:
                await permission.delete()
                return JSONResponse(content={"result": True},status_code=HTTPStatus.OK)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)




# --------------- GET -----------------------


async def get_user(id: UUID):
    try:
        async with db.transaction() as ctx:
            user = await Users.query.where(Users.id == id).gino.first()
            if user:
                return UserSchemaDB.from_orm(user)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def get_group(id: UUID):
    try:
        async with db.transaction() as ctx:
            group = await Groups.query.where(Groups.id == id).gino.first()
            if group:
                return GroupSchemaDB.from_orm(group)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def get_us_gr(id: UUID):
    try:
        async with db.transaction() as ctx:
            group = await User_Groups.query.where(User_Groups.id == id).gino.first()
            if group:
                return UserGroupSchemaDB.from_orm(group)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def get_service(id: UUID):
    try:
        async with db.transaction() as ctx:
            service = await Service.query.where(Service.id == id).gino.first()
            if service:
                return ServiceSchemaDB.from_orm(service)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



async def get_method(id: UUID):
    try:
        async with db.transaction() as ctx:
            method = await Method.query.where(Method.id == id).gino.first()
            if method:
                return MethodSchemaDB.from_orm(method)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)




async def get_permission(id: UUID):
    try:
        async with db.transaction() as ctx:
            permission = await Permission.query.where(Permission.id == id).gino.first()
            if permission:
               return PermissionSchemaDB.from_orm(permission)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)




# --------------- GET ALL-----------------------



async def get_all_user():
    try:
        async with db.transaction() as ctx:
            users = await Users.query.gino.all()
            if users:
                return parse_obj_as(List[UserSchemaDB],users)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def get_all_group():
    try:
        async with db.transaction() as ctx:
            groups = await Groups.query.gino.all()
            if groups:
                return parse_obj_as(List[GroupSchemaDB],groups)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def get_all_us_gr():
    try:
        async with db.transaction() as ctx:
            groups = await User_Groups.query.gino.all()
            if groups:
                return parse_obj_as(List[UserGroupSchemaDB],groups)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)


async def get_all_service():
    try:
        async with db.transaction() as ctx:
            services = await Service.query.gino.all()
            if services:
                return parse_obj_as(List[ServiceSchemaDB],services)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)



async def get_all_method():
    try:
        async with db.transaction() as ctx:
            methods = await Method.query.gino.all()
            if methods:
                return parse_obj_as(List[MethodSchemaDB],methods)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)




async def get_all_permissions():
    try:
        async with db.transaction() as ctx:
            permissions = await Permission.query.gino.all()
            if permissions:
               return parse_obj_as(List[PermissionSchemaDB],permissions)
            return JSONResponse(content={"result": False},status_code=HTTPStatus.NOT_FOUND)
    except Exception as err:
        log.error(f"Error on update_user function ->  {err}")
        return JSONResponse(content={"result": False},status_code=HTTPStatus.BAD_REQUEST)









