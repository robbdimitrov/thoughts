# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import userservice.types_pb2 as types__pb2
import userservice.user_service_pb2 as user__service__pb2


class UserServiceStub(object):
  """Services

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/thoughts.UserService/Create',
        request_serializer=user__service__pb2.UserUpdates.SerializeToString,
        response_deserializer=user__service__pb2.UserResponse.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/thoughts.UserService/GetUser',
        request_serializer=user__service__pb2.UserRequest.SerializeToString,
        response_deserializer=user__service__pb2.UserResponse.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/thoughts.UserService/UpdateUser',
        request_serializer=user__service__pb2.UserUpdates.SerializeToString,
        response_deserializer=types__pb2.Status.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/thoughts.UserService/DeleteUser',
        request_serializer=user__service__pb2.UserRequest.SerializeToString,
        response_deserializer=types__pb2.Status.FromString,
        )


class UserServiceServicer(object):
  """Services

  """

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=user__service__pb2.UserUpdates.FromString,
          response_serializer=user__service__pb2.UserResponse.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=user__service__pb2.UserRequest.FromString,
          response_serializer=user__service__pb2.UserResponse.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=user__service__pb2.UserUpdates.FromString,
          response_serializer=types__pb2.Status.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=user__service__pb2.UserRequest.FromString,
          response_serializer=types__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class FollowServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFollowing = channel.unary_unary(
        '/thoughts.FollowService/GetFollowing',
        request_serializer=user__service__pb2.GetFollowersRequest.SerializeToString,
        response_deserializer=user__service__pb2.Users.FromString,
        )
    self.GetFollowers = channel.unary_unary(
        '/thoughts.FollowService/GetFollowers',
        request_serializer=user__service__pb2.GetFollowersRequest.SerializeToString,
        response_deserializer=user__service__pb2.Users.FromString,
        )
    self.Follow = channel.unary_unary(
        '/thoughts.FollowService/Follow',
        request_serializer=user__service__pb2.FollowRequest.SerializeToString,
        response_deserializer=types__pb2.Status.FromString,
        )
    self.Unfollow = channel.unary_unary(
        '/thoughts.FollowService/Unfollow',
        request_serializer=user__service__pb2.FollowRequest.SerializeToString,
        response_deserializer=types__pb2.Status.FromString,
        )


class FollowServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetFollowing(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFollowers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Follow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Unfollow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FollowServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFollowing': grpc.unary_unary_rpc_method_handler(
          servicer.GetFollowing,
          request_deserializer=user__service__pb2.GetFollowersRequest.FromString,
          response_serializer=user__service__pb2.Users.SerializeToString,
      ),
      'GetFollowers': grpc.unary_unary_rpc_method_handler(
          servicer.GetFollowers,
          request_deserializer=user__service__pb2.GetFollowersRequest.FromString,
          response_serializer=user__service__pb2.Users.SerializeToString,
      ),
      'Follow': grpc.unary_unary_rpc_method_handler(
          servicer.Follow,
          request_deserializer=user__service__pb2.FollowRequest.FromString,
          response_serializer=types__pb2.Status.SerializeToString,
      ),
      'Unfollow': grpc.unary_unary_rpc_method_handler(
          servicer.Unfollow,
          request_deserializer=user__service__pb2.FollowRequest.FromString,
          response_serializer=types__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.FollowService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
