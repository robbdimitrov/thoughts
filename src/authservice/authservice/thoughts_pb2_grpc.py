# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import authservice.thoughts_pb2 as thoughts__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/thoughts.UserService/CreateUser',
                request_serializer=thoughts__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Identifier.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/thoughts.UserService/GetUser',
                request_serializer=thoughts__pb2.UserRequest.SerializeToString,
                response_deserializer=thoughts__pb2.User.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/thoughts.UserService/UpdateUser',
                request_serializer=thoughts__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )
        self.GetFollowing = channel.unary_unary(
                '/thoughts.UserService/GetFollowing',
                request_serializer=thoughts__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Users.FromString,
                )
        self.GetFollowers = channel.unary_unary(
                '/thoughts.UserService/GetFollowers',
                request_serializer=thoughts__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Users.FromString,
                )
        self.FollowUser = channel.unary_unary(
                '/thoughts.UserService/FollowUser',
                request_serializer=thoughts__pb2.UserRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )
        self.UnfollowUser = channel.unary_unary(
                '/thoughts.UserService/UnfollowUser',
                request_serializer=thoughts__pb2.UserRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFollowing(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFollowers(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FollowUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnfollowUser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=thoughts__pb2.CreateUserRequest.FromString,
                    response_serializer=thoughts__pb2.Identifier.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=thoughts__pb2.UserRequest.FromString,
                    response_serializer=thoughts__pb2.User.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=thoughts__pb2.UpdateUserRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
            'GetFollowing': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFollowing,
                    request_deserializer=thoughts__pb2.GetUsersRequest.FromString,
                    response_serializer=thoughts__pb2.Users.SerializeToString,
            ),
            'GetFollowers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFollowers,
                    request_deserializer=thoughts__pb2.GetUsersRequest.FromString,
                    response_serializer=thoughts__pb2.Users.SerializeToString,
            ),
            'FollowUser': grpc.unary_unary_rpc_method_handler(
                    servicer.FollowUser,
                    request_deserializer=thoughts__pb2.UserRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
            'UnfollowUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UnfollowUser,
                    request_deserializer=thoughts__pb2.UserRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'thoughts.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/CreateUser',
            thoughts__pb2.CreateUserRequest.SerializeToString,
            thoughts__pb2.Identifier.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/GetUser',
            thoughts__pb2.UserRequest.SerializeToString,
            thoughts__pb2.User.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/UpdateUser',
            thoughts__pb2.UpdateUserRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFollowing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/GetFollowing',
            thoughts__pb2.GetUsersRequest.SerializeToString,
            thoughts__pb2.Users.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFollowers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/GetFollowers',
            thoughts__pb2.GetUsersRequest.SerializeToString,
            thoughts__pb2.Users.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FollowUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/FollowUser',
            thoughts__pb2.UserRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnfollowUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.UserService/UnfollowUser',
            thoughts__pb2.UserRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSession = channel.unary_unary(
                '/thoughts.AuthService/CreateSession',
                request_serializer=thoughts__pb2.Credentials.SerializeToString,
                response_deserializer=thoughts__pb2.Session.FromString,
                )
        self.GetSession = channel.unary_unary(
                '/thoughts.AuthService/GetSession',
                request_serializer=thoughts__pb2.SessionRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Session.FromString,
                )
        self.DeleteSession = channel.unary_unary(
                '/thoughts.AuthService/DeleteSession',
                request_serializer=thoughts__pb2.SessionRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def CreateSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=thoughts__pb2.Credentials.FromString,
                    response_serializer=thoughts__pb2.Session.SerializeToString,
            ),
            'GetSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSession,
                    request_deserializer=thoughts__pb2.SessionRequest.FromString,
                    response_serializer=thoughts__pb2.Session.SerializeToString,
            ),
            'DeleteSession': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSession,
                    request_deserializer=thoughts__pb2.SessionRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'thoughts.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.AuthService/CreateSession',
            thoughts__pb2.Credentials.SerializeToString,
            thoughts__pb2.Session.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.AuthService/GetSession',
            thoughts__pb2.SessionRequest.SerializeToString,
            thoughts__pb2.Session.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.AuthService/DeleteSession',
            thoughts__pb2.SessionRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class PostServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/thoughts.PostService/CreatePost',
                request_serializer=thoughts__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Identifier.FromString,
                )
        self.GetFeed = channel.unary_unary(
                '/thoughts.PostService/GetFeed',
                request_serializer=thoughts__pb2.GetFeedRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Posts.FromString,
                )
        self.GetPosts = channel.unary_unary(
                '/thoughts.PostService/GetPosts',
                request_serializer=thoughts__pb2.GetPostsRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Posts.FromString,
                )
        self.GetLikedPosts = channel.unary_unary(
                '/thoughts.PostService/GetLikedPosts',
                request_serializer=thoughts__pb2.GetPostsRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Posts.FromString,
                )
        self.GetPost = channel.unary_unary(
                '/thoughts.PostService/GetPost',
                request_serializer=thoughts__pb2.PostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Post.FromString,
                )
        self.DeletePost = channel.unary_unary(
                '/thoughts.PostService/DeletePost',
                request_serializer=thoughts__pb2.PostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )
        self.LikePost = channel.unary_unary(
                '/thoughts.PostService/LikePost',
                request_serializer=thoughts__pb2.PostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )
        self.UnlikePost = channel.unary_unary(
                '/thoughts.PostService/UnlikePost',
                request_serializer=thoughts__pb2.PostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )
        self.RepostPost = channel.unary_unary(
                '/thoughts.PostService/RepostPost',
                request_serializer=thoughts__pb2.PostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )
        self.RemoveRepost = channel.unary_unary(
                '/thoughts.PostService/RemoveRepost',
                request_serializer=thoughts__pb2.PostRequest.SerializeToString,
                response_deserializer=thoughts__pb2.Empty.FromString,
                )


class PostServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeed(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPosts(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLikedPosts(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LikePost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlikePost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RepostPost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveRepost(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=thoughts__pb2.CreatePostRequest.FromString,
                    response_serializer=thoughts__pb2.Identifier.SerializeToString,
            ),
            'GetFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeed,
                    request_deserializer=thoughts__pb2.GetFeedRequest.FromString,
                    response_serializer=thoughts__pb2.Posts.SerializeToString,
            ),
            'GetPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPosts,
                    request_deserializer=thoughts__pb2.GetPostsRequest.FromString,
                    response_serializer=thoughts__pb2.Posts.SerializeToString,
            ),
            'GetLikedPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLikedPosts,
                    request_deserializer=thoughts__pb2.GetPostsRequest.FromString,
                    response_serializer=thoughts__pb2.Posts.SerializeToString,
            ),
            'GetPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPost,
                    request_deserializer=thoughts__pb2.PostRequest.FromString,
                    response_serializer=thoughts__pb2.Post.SerializeToString,
            ),
            'DeletePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePost,
                    request_deserializer=thoughts__pb2.PostRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
            'LikePost': grpc.unary_unary_rpc_method_handler(
                    servicer.LikePost,
                    request_deserializer=thoughts__pb2.PostRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
            'UnlikePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlikePost,
                    request_deserializer=thoughts__pb2.PostRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
            'RepostPost': grpc.unary_unary_rpc_method_handler(
                    servicer.RepostPost,
                    request_deserializer=thoughts__pb2.PostRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
            'RemoveRepost': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveRepost,
                    request_deserializer=thoughts__pb2.PostRequest.FromString,
                    response_serializer=thoughts__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'thoughts.PostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/CreatePost',
            thoughts__pb2.CreatePostRequest.SerializeToString,
            thoughts__pb2.Identifier.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/GetFeed',
            thoughts__pb2.GetFeedRequest.SerializeToString,
            thoughts__pb2.Posts.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/GetPosts',
            thoughts__pb2.GetPostsRequest.SerializeToString,
            thoughts__pb2.Posts.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLikedPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/GetLikedPosts',
            thoughts__pb2.GetPostsRequest.SerializeToString,
            thoughts__pb2.Posts.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/GetPost',
            thoughts__pb2.PostRequest.SerializeToString,
            thoughts__pb2.Post.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/DeletePost',
            thoughts__pb2.PostRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LikePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/LikePost',
            thoughts__pb2.PostRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnlikePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/UnlikePost',
            thoughts__pb2.PostRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RepostPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/RepostPost',
            thoughts__pb2.PostRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveRepost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/thoughts.PostService/RemoveRepost',
            thoughts__pb2.PostRequest.SerializeToString,
            thoughts__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
