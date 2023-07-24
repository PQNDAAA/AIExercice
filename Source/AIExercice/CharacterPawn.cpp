// Fill out your copyright notice in the Description page of Project Settings.


#include "CharacterPawn.h"

#include <algorithm>

#include "GameFramework/SpringArmComponent.h"

// Sets default values
ACharacterPawn::ACharacterPawn()
{
 	// Set this pawn to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void ACharacterPawn::BeginPlay()
{
	Super::BeginPlay();

	APlayerController* PC = Cast<APlayerController>(GetController());

	if(IsValid(PC))
	{
		PC->bShowMouseCursor = true;
		PC->bEnableMouseOverEvents = true;
	}
	
}

// Called every frame
void ACharacterPawn::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
}

// Called to bind functionality to input
void ACharacterPawn::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

FVector ACharacterPawn::ForwardRaycastProto(UCameraComponent* Camera)
{
	FVector CameraWorldLocation = Camera->GetComponentLocation();
	FVector CameraForwardVector = Camera->GetForwardVector();
	FVector RaycastEndLocation = CameraForwardVector * 100000.0f;

	FVector RaycastFinalLocation = CameraWorldLocation + RaycastEndLocation;

	//Raycast Start = CameraWorldLocation
	//Raycast End = RaycastEndLocation 

	return RaycastEndLocation;
}

void ACharacterPawn::MoveActorProto(AActor* actor, FVector loc)
{
	actor->SetActorLocation(loc);
}

void ACharacterPawn::CenterCamera(FVector loc,USpringArmComponent* springArmComponent)
{
	this->SetActorLocation(FVector(loc.X,loc.Y,this->GetActorLocation().Z));
	springArmComponent->SetWorldRotation(FRotator(-50,0,0));
}




