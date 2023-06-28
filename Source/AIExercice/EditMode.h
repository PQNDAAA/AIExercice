// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "IntVectorTypes.h"
#include "GameFramework/Actor.h"
#include "EditMode.generated.h"

UCLASS()
class AIEXERCICE_API AEditMode : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AEditMode();

	UPROPERTY(BlueprintReadWrite,EditAnyWhere, Category = "EditMode")
	float BoxExtentRadius = 80;
	UPROPERTY(BlueprintReadWrite,EditAnyWhere, Category = "EditMode")
	float MaxBoxExtentRadius = 160;

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	UFUNCTION(BlueprintPure, Category="EditMode")
	float CalculateCurrentPourcentage() { return BoxExtentRadius/MaxBoxExtentRadius;}

	UFUNCTION(BlueprintPure,Category="EditMode")
	float CalculateCurrentBoxExtent(float value) {return this->BoxExtentRadius = value * this->MaxBoxExtentRadius;}

};
