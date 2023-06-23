// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "BPManagement_GameMode.generated.h"

/**
 * 
 */
UCLASS()
class AIEXERCICE_API ABPManagement_GameMode : public AGameModeBase
{
	GENERATED_BODY()


public:
	// Sets default values for this pawn's properties
	ABPManagement_GameMode();

protected:

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	UFUNCTION(BlueprintCallable, Category="PlayerStart")
	void PlayerStartLocation(float MapSize,AActor* player);
	
};
