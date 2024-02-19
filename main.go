package main

import (
	"fmt"
	"log"

	"github.com/bwmarrin/discordgo"
	"github.com/mistralll/mawabot/service"
)

type Bot struct {
	discord *discordgo.Session
}

func main() {
	discord, err := service.ConnectToDiscord()
	if err != nil {
		fmt.Println("check 1")
		log.Fatal(err)
	}
	fmt.Println("check 2")

	var bot Bot
	bot.discord = discord
}
