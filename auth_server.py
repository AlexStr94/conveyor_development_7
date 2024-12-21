from uuid import uuid4
import grpc
from concurrent import futures

from auth import auth_pb2
from auth import auth_pb2_grpc


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def CreateUser(self, request):
        response = auth_pb2.UserTokenResponse(token=str(uuid4()))
        return response

    def LoginUserRequest(self, request):
        response = auth_pb2.UserTokenResponse(token=str(uuid4()))
        return response

    def GetUserId(self, request):
        response = auth_pb2.GetUserIdResponse(user=289)
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService, server)
    server.add_insecure_port("[::]:8001")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
