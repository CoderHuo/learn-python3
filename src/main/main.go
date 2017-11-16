package main

import (
	"fmt"
	//"strconv"
	//"net"
	//"reflect"
	//"strings"
	//"syscall"
	//"unicode/utf16"
    "tcp_socket"
    "strings"
)

/*func in(ch chan string, s string) {
	for {
		ch <- "Counting" + s
	}
}*/
var IsSystemDLL = map[string]bool{}

func Add(dll string) string {
	IsSystemDLL[dll] = true
	return dll
}

type Base struct {
	name string
	age  int
}

func (base *Base) Foo() {
	fmt.Println("Base Foo func call", base.name)
	base.name = "haha"
}
func (base *Base) Bar() {
	fmt.Println("Base Bar func call", base.age)
}

type Foo struct {
	name string
	Base
}

const big = 0xFFFFFF

// Decimal to integer.
// Returns number, characters consumed, success.
func dtoi(s string) (n int, i int, ok bool) {
	n = 0
	for i = 0; i < len(s) && '0' <= s[i] && s[i] <= '9'; i++ {
		fmt.Println(s[i])
		n = n*10 + int(s[i]-'0')
		if n >= big {
			return big, i, false
		}
	}
	if i == 0 {
		return 0, 0, false
	}
	return n, i, true
}

type t_int struct{ int }

var v_string = "123"
var index = strings.IndexByte(v_string, '2')

var dateLayouts []string

func init_1() {
	// Generate layouts based on RFC 5322, section 3.3.

	dows := [...]string{"", "Mon, "}   // day-of-week
	days := [...]string{"2", "02"}     // day = 1*2DIGIT
	years := [...]string{"2006", "06"} // year = 4*DIGIT / 2*DIGIT
	seconds := [...]string{":05", ""}  // second
	// "-0700 (MST)" is not in RFC 5322, but is common.
	zones := [...]string{"-0700", "MST", "-0700 (MST)"} // zone = (("+" / "-") 4DIGIT) / "GMT" / ...

	for _, dow := range dows {
		for _, day := range days {
			for _, year := range years {
				for _, second := range seconds {
					for _, zone := range zones {
						s := dow + day + " Jan " + year + " 15:04" + second + " " + zone
						dateLayouts = append(dateLayouts, s)
					}
				}
			}
		}
	}
}

func main() {
    tcp_socket.TCPServer()
	//chs := make(chan string)
	//for i := 0; i < 10; i++ {
	//	go in(chs, strconv.Itoa(i))
	//}
	//for {
	//	fmt.Println(<-chs)
	//}
	/*var base1 Base = Base{"Job", 30}
	base1.Foo()
	base := Base{"huo", 20}
	foo := Foo{"AZaz", Base{"liu", 30}}
	base.Foo()
	foo.Foo()
	fmt.Println(base.name)
	fmt.Println(foo.name)
	fmt.Println(foo.Base.name)
	fmt.Println("hello world!")
	var domain string = "baidu.com"
	fmt.Println(net.LookupHost(domain))
	v, _ := syscall.UTF16PtrFromString(domain)
	fmt.Println("UTF16", *v)
	var value interface{}
	value = *v
	switch t := (value).(type) {
	case string:
		fmt.Println("String", t)
	case int32:
		fmt.Println("INT32")
	case uint16:
		fmt.Println("uint16", t)
	default:
		fmt.Println("----")
	}
	for _, char := range []rune(domain) {
		fmt.Println(char)
	}
	a, _ := syscall.UTF16FromString(domain)
	fmt.Println(a)
	b := utf16.Encode([]rune(domain))
	fmt.Println(b)
	c := utf16.Decode(b)
	fmt.Println(c)
	fmt.Println(syscall.UTF16ToString(b))
	dll := Add("ws2_32.dll")
	fmt.Println(dll)
	dll1 := Add("ws2_32.dll")
	fmt.Println(dll1)
	fmt.Println(IsSystemDLL)
	//tcp_socket.TCPServer()
	type emptyCtx int
	background := new(emptyCtx)
	fmt.Println(background, *background)
	n, i, err := dtoi("udp")
	fmt.Println(n, i, err)
	by := '0'
	s1 := "101"
	fmt.Println(by)
	fmt.Println(int(s1[0] - '0'))

	fmt.Println("-------")
	ch := make(chan int)
	go func() {
		for i := 0; i < 10; i = i + 1 {
			ch <- i
		}
		close(ch)
	}()
	for i := range ch {
		fmt.Println(i)
	}
	fmt.Println(net.DefaultResolver)

	var v_int = 1
	var p_v = &v_int
	var pp_v *int = &v_int
	var v_int1 = &t_int{}
	fmt.Println(p_v, pp_v)
	fmt.Println("type p_v:", reflect.TypeOf(p_v))
	fmt.Println("type net.DefaultResolver:", reflect.TypeOf(net.DefaultResolver))
	fmt.Println("type v_int1:", reflect.TypeOf(v_int1))
	fmt.Println(v_int1)
	fmt.Println(index)
	fmt.Println(v_string[:index+1])
	const (
		max    = uint32(1<<32 - 1)
		cutoff = uint32(1 << 30)
	)
	fmt.Println(max)
	fmt.Println(cutoff)
	init_1()
	for v := range dateLayouts {
		fmt.Println(dateLayouts[v])
	}*/

}
