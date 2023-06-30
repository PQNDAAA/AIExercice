// Fill out your copyright notice in the Description page of Project Settings.


#include "BPManagement_GameMode.h"

#include "CharacterPawn.h"

ABPManagement_GameMode::ABPManagement_GameMode()
{
	// Set this pawn to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

void ABPManagement_GameMode::Tick(float DeltaTime)
{
	
}

void ABPManagement_GameMode::PlayerStartLocation(float MapSize,AActor* Playertarget)
{
	
	float playerStartLocationWorldZ = (MapSize / 1.75f) * 10;
	float playerStartLocationWorldXY = (MapSize/2)*100;

	Playertarget->SetActorLocation(FVector(playerStartLocationWorldXY,playerStartLocationWorldXY,playerStartLocationWorldZ));
	
}


