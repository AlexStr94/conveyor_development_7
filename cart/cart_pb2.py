# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cart.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'cart.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncart.proto\x12\x04\x63\x61rt\"F\n\x17\x41\x64\x64ProductToCartRequest\x12\x0f\n\x07product\x18\x01 \x01(\x03\x12\x0b\n\x03num\x18\x02 \x01(\x05\x12\r\n\x05token\x18\x03 \x01(\t\"8\n\x18\x41\x64\x64ProductToCartResponse\x12\x0f\n\x07product\x18\x01 \x01(\x03\x12\x0b\n\x03num\x18\x02 \x01(\x05\"\'\n\x16GetCartProductsRequest\x12\r\n\x05token\x18\x01 \x01(\t\"K\n\x17GetCartProductsResponse\x12\x30\n\x08products\x18\x01 \x03(\x0b\x32\x1e.cart.AddProductToCartResponse\"\x07\n\x05\x45mpty2\xb0\x01\n\x0b\x43\x61rtService\x12Q\n\x10\x41\x64\x64ProductToCart\x12\x1d.cart.AddProductToCartRequest\x1a\x1e.cart.AddProductToCartResponse\x12N\n\x0fGetCartProducts\x12\x1c.cart.GetCartProductsRequest\x1a\x1d.cart.GetCartProductsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDPRODUCTTOCARTREQUEST']._serialized_start=20
  _globals['_ADDPRODUCTTOCARTREQUEST']._serialized_end=90
  _globals['_ADDPRODUCTTOCARTRESPONSE']._serialized_start=92
  _globals['_ADDPRODUCTTOCARTRESPONSE']._serialized_end=148
  _globals['_GETCARTPRODUCTSREQUEST']._serialized_start=150
  _globals['_GETCARTPRODUCTSREQUEST']._serialized_end=189
  _globals['_GETCARTPRODUCTSRESPONSE']._serialized_start=191
  _globals['_GETCARTPRODUCTSRESPONSE']._serialized_end=266
  _globals['_EMPTY']._serialized_start=268
  _globals['_EMPTY']._serialized_end=275
  _globals['_CARTSERVICE']._serialized_start=278
  _globals['_CARTSERVICE']._serialized_end=454
# @@protoc_insertion_point(module_scope)
