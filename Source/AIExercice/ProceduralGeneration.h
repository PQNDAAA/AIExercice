// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "ProceduralGeneration.generated.h"

UCLASS()
class AIEXERCICE_API AProceduralGeneration : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties

	AProceduralGeneration();

	UPROPERTY(EditAnywhere, Category = "Spawning")
	UClass* ClassToSpawn;

	UPROPERTY(EditAnywhere, Category = "Spawning")
	int32 NumToSpawn;

	UPROPERTY(EditAnywhere, Category = "Spawning")
	FVector SpawnLocation;

	UPROPERTY(EditAnywhere, Category = "Spawning")
	FRotator SpawnRotation;

	
protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	virtual void OnConstruction(const FTransform& Transform) override;
};
