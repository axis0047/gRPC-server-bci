from concurrent import futures
import time

import grpc
import server_pb2
import server_pb2_grpc

class StreamerServicer(server_pb2_grpc.StreamerServicer):
    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = server_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply
    
    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello Request Made:")
        print(request)

        for i in range(3):
            hello_reply = server_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)
            
    def SignalStream(self, request, context):
        return super().SignalStream(request, context)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_StreamerServicer_to_server(StreamerServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()