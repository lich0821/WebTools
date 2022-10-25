#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from fastapi import Body, FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from codec import codec

app = FastAPI()
template = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


@app.get("/re")
async def index(request: Request):
    return template.TemplateResponse("re.html", {"request": request})


@app.get("/codec")
async def index(request: Request):
    return template.TemplateResponse("codec.html", {"request": request})


@app.post("/api/v1/findall")
async def findall(pattern=Body(None), string=Body(None), flags=Body(None)):
    if (not pattern) or (not string):
        return "请输入字符串和正则表达式"

    return str(re.findall(pattern, string))


@app.post("/api/v1/encode")
async def encode(lang=Body(None), msg=Body(None)):
    if not msg:
        return ""
    if lang == "1":
        ret = codec.s2t(msg)
    elif lang == "2":
        ret = codec.s2m(msg)
    else:
        ret = codec.zw_encode(msg, lang)

    return str(ret)


@app.post("/api/v1/decode")
async def decode(lang=Body(None), msg=Body(None)):
    if not msg:
        return ""
    if lang == "1":
        ret = codec.t2s(msg)
    elif lang == "2":
        ret = codec.m2s(msg)
    else:
        ret = codec.zw_decode(msg, lang)

    return ret
