# Zero MQ

Infrastruktura využívající ZeroMQ messaging knihovny.

Obsah:
* python - ukázka peer-to-peer komunikace v jazyce Python
* java - ukázka REST API služby na bázi [SparkJava](http://sparkjava.com/)

Před vlastním spuštěním infrastruktury je nutno nejdříve sestavit Hello World REST API aplikaci v adresáři **java** příkazem
```
    ./gradlew clean distTar
```

Celou infrastrukturu spustíme příkazem
```
    vagrant up
```

Pak můžeme otestovat volání ukázkové REST API aplikace:
```
    curl -H 'Accept: application/json' http://10.0.1.11:8080/hello
```

Výstup by měl vypadat zhruba takto:
```
    { "message": "Hello World from node-1" }
```



