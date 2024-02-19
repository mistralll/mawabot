package main

import (
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
		log.Fatal(err)
	}

	var bot Bot
	bot.discord = discord
}
