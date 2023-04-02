// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Containers/Map.h"
#include "ProceduralGeneration.generated.h"

UCLASS()
class AIEXERCICE_API AProceduralGeneration : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties

	AProceduralGeneration();
	
/*	UPROPERTY(EditAnywhere, Category="GenerationManager")
	TArray<FString> MeshNames;

	UPROPERTY(EditAnywhere, Category="GenerationManager")
	UStaticMesh* Mesh;

	UPROPERTY(EditAnywhere, Category="GenerationManager")
	TArray<UInstancedStaticMeshComponent*> Components;*/
	
protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;


	/*UFUNCTION(BlueprintCallable, Category="GenerationManager")
	void PrintMap();*/
};
