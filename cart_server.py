import grpc
from concurrent import futures

from cart import cart_pb2
from cart import cart_pb2_grpc
from constants import HOSTS, PORTS
from auth import auth_pb2, auth_pb2_grpc


class CartService(cart_pb2_grpc.CartServiceServicer):
    def AddProductToCart(self, request):
        get_user_id_request = auth_pb2.GetUserIdRequest(token=self.token)
        with grpc.insecure_channel(f"{HOSTS["auth"]}:{PORTS["auth"]}") as channel:
            stub = auth_pb2_grpc.AuthServiceStub(channel)
            response = stub.GetUserId(get_user_id_request)
            print(f"USER ID: {response.user}")

        response = cart_pb2.AddProductToCartResponse(product=self.product, num=self.num)

        return response

    def GetCartProducts(self, request):
        response = cart_pb2.GetCartProductsResponse(
            products=[
                cart_pb2.AddProductToCartResponse(product=3, num=1),
                cart_pb2.AddProductToCartResponse(product=8, num=23),
            ]
        )
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    cart_pb2_grpc.add_CartServiceServicer_to_server(CartService, server)
    server.add_insecure_port(f"[::]:{PORTS["cart"]}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
