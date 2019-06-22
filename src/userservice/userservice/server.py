import grpc
from concurrent import futures
import time
import logging

from userservice import thoughts_pb2_grpc
from userservice.user import UserService
from userservice.follow import FollowService
from userservice.auth_client import AuthClient
from userservice.db import Database
from userservice.db_client import DbClient


class Server:
    def __init__(self, port, db_uri, auth_uri):
        self.port = port
        self.db_uri = db_uri
        self.auth_uri = auth_uri

    def create_db_client(self):
        db = Database(self.db_uri)
        db_client = DbClient(db)
        return db_client

    def create_server(self):
        db_client = self.create_db_client()
        auth_client = AuthClient(self.auth_uri)
        user_service = UserService(db_client, auth_client)
        follow_service = FollowService(db_client, auth_client)

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        thoughts_pb2_grpc.add_UserServiceServicer_to_server(user_service, server)
        thoughts_pb2_grpc.add_FollowServiceServicer_to_server(follow_service, server)

        server.add_insecure_port(f'[::]:{self.port}')

        return server

    def serve(self):
        server = self.create_server()
        server.start()
        logging.info(f'Server running on port {self.port}')
        try:
            while True:
                time.sleep(60 * 60 * 24)
        except KeyboardInterrupt:
            server.stop(0)
