// Fill out your copyright notice in the Description page of Project Settings.


#include "MyBlueprintFunctionLibrary.h"

#include "MyActor.h"
#include "Materials/MaterialInstance.h"
#include "Kismet/GameplayStatics.h"

void UMyBlueprintFunctionLibrary::Print(FString message)
{
#if UE_EDITOR
	GEngine->AddOnScreenDebugMessage(-1, 15.0f, FColor::Red, message);
#endif
		UE_LOG(LogTemp, Log, TEXT("%s"), *message);
}

void UMyBlueprintFunctionLibrary::ToggleAllLights()
{
	UWorld* world = GEngine->GameViewport->GetWorld();

	TArray<AActor*> Actors;
	UGameplayStatics::GetAllActorsOfClass(
		world,
		AMyActor::StaticClass(),
		Actors);

	for (AActor* tmp : Actors)
	{
		((AMyActor*)tmp)->ToggleVisibility();
	}

	
}

void UMyBlueprintFunctionLibrary::SetMaterialInstanceStaticSwitchParameterValue(UMaterialInstance* Instance, FName ParamaterName, bool value)
{
	FStaticParameterSet StaticParameters = Instance->GetStaticParameters();

	for (auto& SwitchParam : StaticParameters.StaticSwitchParameters)
	{
		if(SwitchParam.ParameterInfo.Name == ParamaterName)
		{
			SwitchParam.Value = value;
			break;;
		}
	}
	//Instance->UpdateStaticPermutation(StaticParameters);
}


