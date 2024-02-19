package discord

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"github.com/bwmarrin/discordgo"
	"github.com/joho/godotenv"
)

func ConnectToDiscord() (*discordgo.Session, error) {
	err := godotenv.Load(".env")
	if err != nil {
		fmt.Println("Fail to load env.")
		return nil, err
	}

	token := "Bot " + os.Getenv("APP_BOT_TOKEN")

	fmt.Println(token)

	dg, err := discordgo.New(token)
	if err != nil {
		fmt.Println("Fail to login.")
		return nil, err
	}

	// discord.AddHandler()
	
	err = dg.Open()
	if err != nil {
		return nil, err
	}

	defer dg.Close()

	fmt.Println("Listening...")

	stopBot := make(chan os.Signal, 1)
	signal.Notify(stopBot, syscall.SIGINT, syscall.SIGTERM, os.Interrupt)
	<-stopBot

	return dg, nil
}
