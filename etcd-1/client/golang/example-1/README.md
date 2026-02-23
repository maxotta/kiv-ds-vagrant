go mod init kiv-dsa/etcd/client  => init module
go mod tidy => create dependency file from source and download dependencies

Go intro: https://go.dev/doc/effective_go

// https://faun.pub/understanding-go-mod-and-go-sum-5fd7ec9bcc34
// https://medium.com/@felipedutratine/distributed-lock-with-etcd-in-go-d21e7df145bc
// https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
// https://medium.com/@felipedutratine/leader-election-in-go-with-etcd-2ca8f3876d79

// https://github.com/etcd-io/etcd/tree/main/tests/integration/clientv3/examples

// func (op OpResponse) Put() *PutResponse    { return op.put }
// func (op OpResponse) Get() *GetResponse    { return op.get }
// func (op OpResponse) Del() *DeleteResponse { return op.del }
// func (op OpResponse) Txn() *TxnResponse    { return op.txn }

# Example 1 - set/get/delete KV
# Example 2 - get KV range
# Example 3 - entry versions
# Example 4 - key watches
# Example 5 - lease - attach a lease to a KV
# Example 6 - mutex
# Example 7 - transaction
# Example 8 - election

https://etcd.io/docs/v3.5/tutorials/
https://etcd.io/docs/v3.5/dev-internal/modules/
https://pkg.go.dev/github.com/coreos/etcd/clientv3/concurrency  <<<<

https://amyangfei.me/2020/12/19/best-practice-with-go-etcd/

https://etcd.io/docs/v3.5/integrations/
