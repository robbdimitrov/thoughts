# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thoughts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ethoughts.proto\x12\x08thoughts\"T\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"\x18\n\nIdentifier\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\xc5\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x05 \x01(\t\x12\x0b\n\x03\x62io\x18\x06 \x01(\t\x12\r\n\x05posts\x18\x07 \x01(\x05\x12\r\n\x05likes\x18\x08 \x01(\x05\x12\x11\n\tfollowing\x18\t \x01(\x05\x12\x11\n\tfollowers\x18\n \x01(\x05\x12\x10\n\x08\x66ollowed\x18\x0b \x01(\x08\x12\x0f\n\x07\x63reated\x18\x0c \x01(\t\"\x87\x01\n\x11UpdateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x14\n\x0cold_password\x18\x05 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x06 \x01(\t\x12\x0b\n\x03\x62io\x18\x07 \x01(\t\"?\n\x0fGetUsersRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\"&\n\x05Users\x12\x1d\n\x05users\x18\x01 \x03(\x0b\x32\x0e.thoughts.User\"\x07\n\x05\x45mpty\".\n\x0b\x43redentials\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"$\n\x0eSessionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"7\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x63reated\x18\x03 \x01(\t\"$\n\x11\x43reatePostRequest\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x1e\n\x0bPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\x05\"\x86\x01\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\r\n\x05likes\x18\x04 \x01(\x05\x12\r\n\x05liked\x18\x05 \x01(\x08\x12\x0f\n\x07reposts\x18\x06 \x01(\x05\x12\x10\n\x08reposted\x18\x07 \x01(\x08\x12\x0f\n\x07\x63reated\x18\x08 \x01(\t\"-\n\x0eGetFeedRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"&\n\x05Posts\x12\x1d\n\x05posts\x18\x01 \x03(\x0b\x32\x0e.thoughts.Post\"?\n\x0fGetPostsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x32\xa2\x03\n\x0bUserService\x12?\n\nCreateUser\x12\x1b.thoughts.CreateUserRequest\x1a\x14.thoughts.Identifier\x12\x30\n\x07GetUser\x12\x15.thoughts.UserRequest\x1a\x0e.thoughts.User\x12:\n\nUpdateUser\x12\x1b.thoughts.UpdateUserRequest\x1a\x0f.thoughts.Empty\x12:\n\x0cGetFollowing\x12\x19.thoughts.GetUsersRequest\x1a\x0f.thoughts.Users\x12:\n\x0cGetFollowers\x12\x19.thoughts.GetUsersRequest\x1a\x0f.thoughts.Users\x12\x34\n\nFollowUser\x12\x15.thoughts.UserRequest\x1a\x0f.thoughts.Empty\x12\x36\n\x0cUnfollowUser\x12\x15.thoughts.UserRequest\x1a\x0f.thoughts.Empty2\xbf\x01\n\x0b\x41uthService\x12\x39\n\rCreateSession\x12\x15.thoughts.Credentials\x1a\x11.thoughts.Session\x12\x39\n\nGetSession\x12\x18.thoughts.SessionRequest\x1a\x11.thoughts.Session\x12:\n\rDeleteSession\x12\x18.thoughts.SessionRequest\x1a\x0f.thoughts.Empty2\xb9\x04\n\x0bPostService\x12?\n\nCreatePost\x12\x1b.thoughts.CreatePostRequest\x1a\x14.thoughts.Identifier\x12\x34\n\x07GetFeed\x12\x18.thoughts.GetFeedRequest\x1a\x0f.thoughts.Posts\x12\x36\n\x08GetPosts\x12\x19.thoughts.GetPostsRequest\x1a\x0f.thoughts.Posts\x12;\n\rGetLikedPosts\x12\x19.thoughts.GetPostsRequest\x1a\x0f.thoughts.Posts\x12\x30\n\x07GetPost\x12\x15.thoughts.PostRequest\x1a\x0e.thoughts.Post\x12\x34\n\nDeletePost\x12\x15.thoughts.PostRequest\x1a\x0f.thoughts.Empty\x12\x32\n\x08LikePost\x12\x15.thoughts.PostRequest\x1a\x0f.thoughts.Empty\x12\x34\n\nUnlikePost\x12\x15.thoughts.PostRequest\x1a\x0f.thoughts.Empty\x12\x34\n\nRepostPost\x12\x15.thoughts.PostRequest\x1a\x0f.thoughts.Empty\x12\x36\n\x0cRemoveRepost\x12\x15.thoughts.PostRequest\x1a\x0f.thoughts.EmptyB\x0cZ\n./genprotob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thoughts_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./genproto'
  _CREATEUSERREQUEST._serialized_start=28
  _CREATEUSERREQUEST._serialized_end=112
  _IDENTIFIER._serialized_start=114
  _IDENTIFIER._serialized_end=138
  _USERREQUEST._serialized_start=140
  _USERREQUEST._serialized_end=170
  _USER._serialized_start=173
  _USER._serialized_end=370
  _UPDATEUSERREQUEST._serialized_start=373
  _UPDATEUSERREQUEST._serialized_end=508
  _GETUSERSREQUEST._serialized_start=510
  _GETUSERSREQUEST._serialized_end=573
  _USERS._serialized_start=575
  _USERS._serialized_end=613
  _EMPTY._serialized_start=615
  _EMPTY._serialized_end=622
  _CREDENTIALS._serialized_start=624
  _CREDENTIALS._serialized_end=670
  _SESSIONREQUEST._serialized_start=672
  _SESSIONREQUEST._serialized_end=708
  _SESSION._serialized_start=710
  _SESSION._serialized_end=765
  _CREATEPOSTREQUEST._serialized_start=767
  _CREATEPOSTREQUEST._serialized_end=803
  _POSTREQUEST._serialized_start=805
  _POSTREQUEST._serialized_end=835
  _POST._serialized_start=838
  _POST._serialized_end=972
  _GETFEEDREQUEST._serialized_start=974
  _GETFEEDREQUEST._serialized_end=1019
  _POSTS._serialized_start=1021
  _POSTS._serialized_end=1059
  _GETPOSTSREQUEST._serialized_start=1061
  _GETPOSTSREQUEST._serialized_end=1124
  _USERSERVICE._serialized_start=1127
  _USERSERVICE._serialized_end=1545
  _AUTHSERVICE._serialized_start=1548
  _AUTHSERVICE._serialized_end=1739
  _POSTSERVICE._serialized_start=1742
  _POSTSERVICE._serialized_end=2311
# @@protoc_insertion_point(module_scope)
