package main

import (
	"fmt"
	"os/exec"
	"gopkg.in/gomail.v2"
	"time"
	"math/rand"
)

func ExecCommand(name string, arg ...string) string {
	cmd := exec.Command(name, arg...)
	info, err := cmd.Output()
	if err != nil {
		fmt.Println(info)
	}
	fmt.Println(string(info))
	return string(info)
}

func SendToEmail(msg string) {
	m := gomail.NewMessage()
	m.SetHeader("From", "xxxx@xxxx.com")
	m.SetHeader("To", "xxxx@xxxx.com")
	m.SetHeader("Subject", "start日志")
	m.SetBody("text/html", msg)
	d := gomail.NewDialer("xxxx@xxxx.com", 25, "xxxx@xxxx.com", "xxxx@xxxx.com")
	if err := d.DialAndSend(m); err != nil {
		fmt.Println(err.Error())
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	sleep := time.Duration(rand.Int31n(3600)) * time.Second
	msg := fmt.Sprintf("will be sleep: %v", sleep)
	fmt.Println(msg)
	time.Sleep(sleep)
	msg = fmt.Sprintf("%s<br/>%s", msg, ExecCommand("python3", "WangYiCoin.py"))
	SendToEmail(msg)
}