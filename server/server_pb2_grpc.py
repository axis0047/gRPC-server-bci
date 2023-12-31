# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class StreamerStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/streamServer.Streamer/SayHello',
                request_serializer=server__pb2.HelloRequest.SerializeToString,
                response_deserializer=server__pb2.HelloReply.FromString,
                )
        self.ParrotSaysHello = channel.unary_stream(
                '/streamServer.Streamer/ParrotSaysHello',
                request_serializer=server__pb2.HelloRequest.SerializeToString,
                response_deserializer=server__pb2.HelloReply.FromString,
                )
        self.SignalStream = channel.unary_stream(
                '/streamServer.Streamer/SignalStream',
                request_serializer=server__pb2.SignalRequest.SerializeToString,
                response_deserializer=server__pb2.SignalReply.FromString,
                )


class StreamerServicer(object):
    """The greeting service definition.
    """

    def SayHello(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ParrotSaysHello(self, request, context):
        """Server Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignalStream(self, request, context):
        """Server Streaming signal
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=server__pb2.HelloRequest.FromString,
                    response_serializer=server__pb2.HelloReply.SerializeToString,
            ),
            'ParrotSaysHello': grpc.unary_stream_rpc_method_handler(
                    servicer.ParrotSaysHello,
                    request_deserializer=server__pb2.HelloRequest.FromString,
                    response_serializer=server__pb2.HelloReply.SerializeToString,
            ),
            'SignalStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SignalStream,
                    request_deserializer=server__pb2.SignalRequest.FromString,
                    response_serializer=server__pb2.SignalReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'streamServer.Streamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Streamer(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/streamServer.Streamer/SayHello',
            server__pb2.HelloRequest.SerializeToString,
            server__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ParrotSaysHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/streamServer.Streamer/ParrotSaysHello',
            server__pb2.HelloRequest.SerializeToString,
            server__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignalStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/streamServer.Streamer/SignalStream',
            server__pb2.SignalRequest.SerializeToString,
            server__pb2.SignalReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
