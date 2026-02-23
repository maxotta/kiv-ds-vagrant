/*
 * Simple client example - get a range of keys
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

	APP_PREFIX        = "etcd-client-app."
	KEY_JDBC_URL      = APP_PREFIX + "jdbc_url"
	KEY_JDBC_USER     = APP_PREFIX + "jdbc_user"
	KEY_JDBC_PASSWORD = APP_PREFIX + "jdbc_password"
)

func main() {

	fmt.Println("Demo client 2:")

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
	// Put a key-value pair
	_, err = cli.Put(ctx, KEY_JDBC_USER, "admin")
	if err != nil {
		log.Fatal(err)
	}
	// Put a key-value pair
	_, err = cli.Put(ctx, KEY_JDBC_PASSWORD, "sc3r3t+k3y")
	if err != nil {
		log.Fatal(err)
	}

	// Get all keys with the prefix
	val, err := cli.Get(ctx, APP_PREFIX, clientv3.WithPrefix())
	if err != nil {
		log.Fatal(err)
	}
	if len(val.Kvs) > 0 {
		for _, kv := range val.Kvs {
			fmt.Printf("Key: %s, Value: %s\n", kv.Key, kv.Value)
		}
	} else {
		fmt.Printf("No keys found with the prefix '%s'\n", APP_PREFIX)
	}

	// Delete keys with the prefix
	_, err = cli.Delete(ctx, APP_PREFIX, clientv3.WithPrefix())
	if err != nil {
		log.Fatal(err)
	}
	// Try to get the deleted keys
	val, err = cli.Get(ctx, APP_PREFIX, clientv3.WithPrefix())
	if err != nil {
		log.Fatal(err)
	}
	if len(val.Kvs) > 0 {
		fmt.Printf("There are still %d keys with the prefix '%s'\n", len(val.Kvs), APP_PREFIX)
	} else {
		fmt.Printf("No keys found with the prefix '%s'\n", APP_PREFIX)
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
