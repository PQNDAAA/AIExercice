// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Camera/CameraComponent.h"
#include "GameFramework/Pawn.h"
#include "GameFramework/SpringArmComponent.h"
#include "CharacterPawn.generated.h"

UCLASS()
class AIEXERCICE_API ACharacterPawn : public APawn
{
	GENERATED_BODY()

public:
	// Sets default values for this pawn's properties
	ACharacterPawn();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

	UFUNCTION(BlueprintCallable, Category="ConstructionMode")
	FVector ForwardRaycastProto(UCameraComponent* Camera);

	UFUNCTION(BlueprintCallable, Category="ConstructionMode")
	void MoveActorProto(AActor* actor, FVector loc);

	UFUNCTION(BlueprintCallable, Category="CenterCamera")
	void CenterCamera(FVector loc,USpringArmComponent* springArmComponent);

};
