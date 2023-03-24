// Fill out your copyright notice in the Description page of Project Settings.


#include "MyActor.h"

// Sets default values
AMyActor::AMyActor()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	this->intensity = 3000.0f;
	this->isActive = true;

	this->PointLight = CreateDefaultSubobject<UPointLightComponent>(TEXT("Point Light"));
	this->PointLight->Intensity = this->intensity;
	this->PointLight->SetVisibility(true);
	this->PointLight->SetupAttachment(RootComponent);

}

// Called when the game starts or when spawned
void AMyActor::BeginPlay()
{
	Super::BeginPlay();

	this->PointLight->SetVisibility(this->isVisibleAtStart);
}

// Called every frame
void AMyActor::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void AMyActor::ToggleVisibility()
{
	this->PointLight->ToggleVisibility();
}


