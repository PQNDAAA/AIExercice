// Fill out your copyright notice in the Description page of Project Settings.


#include "ProceduralGeneration.h"

#include "ComponentUtils.h"
#include "Components/InstancedStaticMeshComponent.h"

// Sets default values
AProceduralGeneration::AProceduralGeneration()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	
	USceneComponent* Root = CreateDefaultSubobject<USceneComponent>(TEXT("Root"));
	RootComponent = Root;
}

// Called when the game starts or when spawned
void AProceduralGeneration::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AProceduralGeneration::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

/*void AProceduralGeneration::PrintMap()
{
	for (const FString& Name : this->MeshNames)
	{
		// Créer un nouvel objet UInstancedStaticMeshComponent pour chaque élément du tableau
		UInstancedStaticMeshComponent* NewComponent = NewObject<UInstancedStaticMeshComponent>(this, FName(*Name));
		if (NewComponent)
		{
			// Configurer le composant comme souhaité
			NewComponent->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);
			//NewComponent->SetStaticMesh(Mesh);

			if(!Components.Contains(NewComponent))
			{
				// Ajouter le composant au tableau Components
				Components.Add(NewComponent);
			}
		}
	}
}*/



