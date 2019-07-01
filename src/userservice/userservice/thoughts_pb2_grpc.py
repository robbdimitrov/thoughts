# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import userservice.thoughts_pb2 as thoughts__pb2


class UserServiceStub(object):
  """*
  Services

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUser = channel.unary_unary(
        '/thoughts.UserService/CreateUser',
        request_serializer=thoughts__pb2.UserUpdates.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/thoughts.UserService/GetUser',
        request_serializer=thoughts__pb2.UserRequest.SerializeToString,
        response_deserializer=thoughts__pb2.UserStatus.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/thoughts.UserService/UpdateUser',
        request_serializer=thoughts__pb2.UserUpdates.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.UpdatePassword = channel.unary_unary(
        '/thoughts.UserService/UpdatePassword',
        request_serializer=thoughts__pb2.UserUpdates.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/thoughts.UserService/DeleteUser',
        request_serializer=thoughts__pb2.UserRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )


class UserServiceServicer(object):
  """*
  Services

  """

  def CreateUser(self, request, context):
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

  def UpdatePassword(self, request, context):
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
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=thoughts__pb2.UserUpdates.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=thoughts__pb2.UserRequest.FromString,
          response_serializer=thoughts__pb2.UserStatus.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=thoughts__pb2.UserUpdates.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'UpdatePassword': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePassword,
          request_deserializer=thoughts__pb2.UserUpdates.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=thoughts__pb2.UserRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
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
        request_serializer=thoughts__pb2.DataRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Users.FromString,
        )
    self.GetFollowingIds = channel.unary_unary(
        '/thoughts.FollowService/GetFollowingIds',
        request_serializer=thoughts__pb2.UserRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Identifiers.FromString,
        )
    self.GetFollowers = channel.unary_unary(
        '/thoughts.FollowService/GetFollowers',
        request_serializer=thoughts__pb2.DataRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Users.FromString,
        )
    self.GetFollowersIds = channel.unary_unary(
        '/thoughts.FollowService/GetFollowersIds',
        request_serializer=thoughts__pb2.UserRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Identifiers.FromString,
        )
    self.FollowUser = channel.unary_unary(
        '/thoughts.FollowService/FollowUser',
        request_serializer=thoughts__pb2.UserRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.UnfollowUser = channel.unary_unary(
        '/thoughts.FollowService/UnfollowUser',
        request_serializer=thoughts__pb2.UserRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
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

  def GetFollowingIds(self, request, context):
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

  def GetFollowersIds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FollowUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnfollowUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FollowServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFollowing': grpc.unary_unary_rpc_method_handler(
          servicer.GetFollowing,
          request_deserializer=thoughts__pb2.DataRequest.FromString,
          response_serializer=thoughts__pb2.Users.SerializeToString,
      ),
      'GetFollowingIds': grpc.unary_unary_rpc_method_handler(
          servicer.GetFollowingIds,
          request_deserializer=thoughts__pb2.UserRequest.FromString,
          response_serializer=thoughts__pb2.Identifiers.SerializeToString,
      ),
      'GetFollowers': grpc.unary_unary_rpc_method_handler(
          servicer.GetFollowers,
          request_deserializer=thoughts__pb2.DataRequest.FromString,
          response_serializer=thoughts__pb2.Users.SerializeToString,
      ),
      'GetFollowersIds': grpc.unary_unary_rpc_method_handler(
          servicer.GetFollowersIds,
          request_deserializer=thoughts__pb2.UserRequest.FromString,
          response_serializer=thoughts__pb2.Identifiers.SerializeToString,
      ),
      'FollowUser': grpc.unary_unary_rpc_method_handler(
          servicer.FollowUser,
          request_deserializer=thoughts__pb2.UserRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'UnfollowUser': grpc.unary_unary_rpc_method_handler(
          servicer.UnfollowUser,
          request_deserializer=thoughts__pb2.UserRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.FollowService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AuthServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Login = channel.unary_unary(
        '/thoughts.AuthService/Login',
        request_serializer=thoughts__pb2.Credentials.SerializeToString,
        response_deserializer=thoughts__pb2.AuthStatus.FromString,
        )
    self.Refresh = channel.unary_unary(
        '/thoughts.AuthService/Refresh',
        request_serializer=thoughts__pb2.AuthRequest.SerializeToString,
        response_deserializer=thoughts__pb2.AuthStatus.FromString,
        )
    self.Validate = channel.unary_unary(
        '/thoughts.AuthService/Validate',
        request_serializer=thoughts__pb2.AuthRequest.SerializeToString,
        response_deserializer=thoughts__pb2.AuthStatus.FromString,
        )
    self.ValidatePassword = channel.unary_unary(
        '/thoughts.AuthService/ValidatePassword',
        request_serializer=thoughts__pb2.Credentials.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )


class AuthServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Refresh(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Validate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ValidatePassword(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=thoughts__pb2.Credentials.FromString,
          response_serializer=thoughts__pb2.AuthStatus.SerializeToString,
      ),
      'Refresh': grpc.unary_unary_rpc_method_handler(
          servicer.Refresh,
          request_deserializer=thoughts__pb2.AuthRequest.FromString,
          response_serializer=thoughts__pb2.AuthStatus.SerializeToString,
      ),
      'Validate': grpc.unary_unary_rpc_method_handler(
          servicer.Validate,
          request_deserializer=thoughts__pb2.AuthRequest.FromString,
          response_serializer=thoughts__pb2.AuthStatus.SerializeToString,
      ),
      'ValidatePassword': grpc.unary_unary_rpc_method_handler(
          servicer.ValidatePassword,
          request_deserializer=thoughts__pb2.Credentials.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.AuthService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SessionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSessions = channel.unary_unary(
        '/thoughts.SessionService/GetSessions',
        request_serializer=thoughts__pb2.AuthRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Sessions.FromString,
        )
    self.DeleteSession = channel.unary_unary(
        '/thoughts.SessionService/DeleteSession',
        request_serializer=thoughts__pb2.SessionRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )


class SessionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSessions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SessionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSessions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSessions,
          request_deserializer=thoughts__pb2.AuthRequest.FromString,
          response_serializer=thoughts__pb2.Sessions.SerializeToString,
      ),
      'DeleteSession': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSession,
          request_deserializer=thoughts__pb2.SessionRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.SessionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PostServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreatePost = channel.unary_unary(
        '/thoughts.PostService/CreatePost',
        request_serializer=thoughts__pb2.PostUpdates.SerializeToString,
        response_deserializer=thoughts__pb2.PostStatus.FromString,
        )
    self.GetPost = channel.unary_unary(
        '/thoughts.PostService/GetPost',
        request_serializer=thoughts__pb2.PostRequest.SerializeToString,
        response_deserializer=thoughts__pb2.PostStatus.FromString,
        )
    self.GetFeed = channel.unary_unary(
        '/thoughts.PostService/GetFeed',
        request_serializer=thoughts__pb2.DataRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Posts.FromString,
        )
    self.GetPosts = channel.unary_unary(
        '/thoughts.PostService/GetPosts',
        request_serializer=thoughts__pb2.DataRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Posts.FromString,
        )
    self.GetLikedPosts = channel.unary_unary(
        '/thoughts.PostService/GetLikedPosts',
        request_serializer=thoughts__pb2.DataRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Posts.FromString,
        )
    self.DeletePost = channel.unary_unary(
        '/thoughts.PostService/DeletePost',
        request_serializer=thoughts__pb2.PostRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )


class PostServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreatePost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPosts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLikedPosts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreatePost': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePost,
          request_deserializer=thoughts__pb2.PostUpdates.FromString,
          response_serializer=thoughts__pb2.PostStatus.SerializeToString,
      ),
      'GetPost': grpc.unary_unary_rpc_method_handler(
          servicer.GetPost,
          request_deserializer=thoughts__pb2.PostRequest.FromString,
          response_serializer=thoughts__pb2.PostStatus.SerializeToString,
      ),
      'GetFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeed,
          request_deserializer=thoughts__pb2.DataRequest.FromString,
          response_serializer=thoughts__pb2.Posts.SerializeToString,
      ),
      'GetPosts': grpc.unary_unary_rpc_method_handler(
          servicer.GetPosts,
          request_deserializer=thoughts__pb2.DataRequest.FromString,
          response_serializer=thoughts__pb2.Posts.SerializeToString,
      ),
      'GetLikedPosts': grpc.unary_unary_rpc_method_handler(
          servicer.GetLikedPosts,
          request_deserializer=thoughts__pb2.DataRequest.FromString,
          response_serializer=thoughts__pb2.Posts.SerializeToString,
      ),
      'DeletePost': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePost,
          request_deserializer=thoughts__pb2.PostRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.PostService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ActionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.LikePost = channel.unary_unary(
        '/thoughts.ActionService/LikePost',
        request_serializer=thoughts__pb2.PostRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.UnlikePost = channel.unary_unary(
        '/thoughts.ActionService/UnlikePost',
        request_serializer=thoughts__pb2.PostRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.RetweetPost = channel.unary_unary(
        '/thoughts.ActionService/RetweetPost',
        request_serializer=thoughts__pb2.PostRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )
    self.RemoveRetweet = channel.unary_unary(
        '/thoughts.ActionService/RemoveRetweet',
        request_serializer=thoughts__pb2.PostRequest.SerializeToString,
        response_deserializer=thoughts__pb2.Status.FromString,
        )


class ActionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def LikePost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnlikePost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RetweetPost(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveRetweet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ActionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'LikePost': grpc.unary_unary_rpc_method_handler(
          servicer.LikePost,
          request_deserializer=thoughts__pb2.PostRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'UnlikePost': grpc.unary_unary_rpc_method_handler(
          servicer.UnlikePost,
          request_deserializer=thoughts__pb2.PostRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'RetweetPost': grpc.unary_unary_rpc_method_handler(
          servicer.RetweetPost,
          request_deserializer=thoughts__pb2.PostRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
      'RemoveRetweet': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveRetweet,
          request_deserializer=thoughts__pb2.PostRequest.FromString,
          response_serializer=thoughts__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'thoughts.ActionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
