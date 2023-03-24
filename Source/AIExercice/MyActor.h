// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Components/PointLightComponent.h"
#include "MyActor.generated.h"

UCLASS()
class AIEXERCICE_API AMyActor : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AMyActor();

	UPROPERTY(EditAnyWhere, Category = "Custom Light")
		float intensity;
	UPROPERTY(EditAnyWhere, Category = "Custom Light")
		bool isVisibleAtStart;
	UPROPERTY(EditAnyWhere, Category = "Custom Light")
		bool isActive;
	UPROPERTY(VisibleAnyWhere, Category = "Custom Light")
		UPointLightComponent* PointLight;
	

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	UFUNCTION(BlueprintCallable, Category="CustomLight")
	void ToggleVisibility();

};
