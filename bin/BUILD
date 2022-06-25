package(default_visibility = ["//visibility:public"])
load("//:doctest.bzl", "py_doc_test")

py_binary (
    name = "main",
    srcs = glob(["main.py"]),
)

py_doc_test(
  name="doc_test",
  deps = [":main"],
)
