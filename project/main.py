from run.utils import _create_deployment, delete_deployment, _copy_file_to_image, _add_service, \
     _get_pod_logs, _get_deployment_logs
from project.api.po_servers.api import api_router
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import pwd

def main():


    app = FastAPI(title="FLAME PO",
                  docs_url="/api/docs",
                  redoc_url="/api/redoc",
                  openapi_url="/api/v1/openapi.json", )

    origins = [
        "http://localhost:8080/",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(
        api_router,
        prefix="/api",
    )

    # server = PoBaseServer()

    #create_deployment("hallo-world", "karthequian/helloworld:latest", [80, 443])

    #uvicorn.run(app, host="0.0.0.0", port=8000)

    #_create_deployment( "testapp", "testapp:latest", [80, 443])
    #delete_deployment("ubuntu-test3")
    #get_deployment_logs("helloworld")
    #_copy_file_to_image("testapp:latest", "/home/davidhieber/PycharmProjects/node-pod-orchestration/project/test.txt", "/opt/test.txt")
    #_add_service("testapp", 80, 443)
    # Get the effective user ID (uid) and group ID (gid)
    #uid = os.geteuid()
    #gid = os.getegid()

#print(_get_pod_logs("testapp-7f4c4cbf58-vp4mj"))
    _get_deployment_logs("testapp")
if __name__ == '__main__':

    main()

