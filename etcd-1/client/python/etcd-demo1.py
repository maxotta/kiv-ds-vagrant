import etcd3

etcd = etcd3.client(host="10.0.1.11")

etcd.put("foo", "bar")
value, metadata = etcd.get("foo")
print("Value:", value.decode())
