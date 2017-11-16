package tcp_socket

import (
    "fmt"
    "net"
    "log"
    "runtime"
)

func handleConnect(conn net.Conn) {
    clientAddr := conn.RemoteAddr()
    defer conn.Close()
    buff := make([]byte, 2048)
    for {
        n, err := conn.Read(buff)
        if err != nil {
            fmt.Println("haha", err)
            break
        }
        resp := []byte("HTTP/1.1 200 OK\r\nDate: Wed, 10 Jun 2009 11:22:58 GMT\r\nServer: Microsoft-IIS/6" +
            ".0\r\nX-Powered-By: ASP.NET\r\nContent-Length: 119\r\nContent-Type: text/html\r\n\r\n" +
            "<!DOCTYPE html>\r\n" +
            "<!--STATUS OK-->\r\n" +
            "<html>\r\n" +
            "<head>\r\n<title>hello</title>\r\n</head>\r\n" +
            "<body>\r\nHello World\r\n</body>\r\n" +
            "</html>\r\n")
        conn.Write(resp)
        //fmt.Println(clientAddr, string(resp))
        fmt.Println(clientAddr, string(buff[:n]))
    }
}

func TCPServer() {
    serverAddr := "0.0.0.0:30000"
    listener, err := net.Listen("tcp", serverAddr)
    if err != nil {
        log.Fatal(err)
    }
    defer listener.Close()
    for {
        conn, err := listener.Accept()
        if err != nil {
            log.Fatal(err)
        }
        go handleConnect(conn)
        fmt.Println(runtime.NumGoroutine())
    }
}
