/*
 * Simple client example - put and get a key, delete a key
 */

package main

import (
	"context"
	"fmt"
	"log"
	"time"

	clientv3 "go.etcd.io/etcd/client/v3"
)

const (
	dialTimeout    = 5 * time.Second
	requestTimeout = 10 * time.Second

	KEY_JDBC_URL = "jdbc_url"
)

func main() {

	fmt.Println("Demo client 1:")

	cli, err := clientv3.New(clientv3.Config{
		Endpoints:   []string{"etcd-1:2379", "etcd-2:2379", "etcd-3:2379"},
		DialTimeout: dialTimeout,
	})
	if err != nil {
		log.Fatal(err)
	}
	defer cli.Close()

	// Create a context with a timeout for the following operations
	ctx, cancel := context.WithTimeout(context.Background(), requestTimeout)

	// Put a key-value pair
	_, err = cli.Put(ctx, KEY_JDBC_URL, "jdbc:mysql://localhost:3306/test?useSSL=false")
	if err != nil {
		log.Fatal(err)
	}

	// Get the value for the key
	val, err := cli.Get(ctx, KEY_JDBC_URL)
	if err != nil {
		log.Fatal(err)
	}
	if len(val.Kvs) > 0 {
		fmt.Printf("Key: %s, Value: %s\n", val.Kvs[0].Key, val.Kvs[0].Value)
	} else {
		fmt.Println("Key not found")
	}

	// Delete the key
	_, err = cli.Delete(ctx, KEY_JDBC_URL)
	if err != nil {
		log.Fatal(err)
	}
	// Try to get the deleted key
	val, err = cli.Get(ctx, KEY_JDBC_URL)
	if err != nil {
		log.Fatal(err)
	}
	if len(val.Kvs) > 0 {
		fmt.Printf("Key: %s, Value: %s\n", val.Kvs[0].Key, val.Kvs[0].Value)
	} else {
		fmt.Println("Key not found")
	}

	// Cancel the timeout context
	cancel()
	if err != nil {
		log.Fatal(err)
	}
}

/*
 * EOF
 */
