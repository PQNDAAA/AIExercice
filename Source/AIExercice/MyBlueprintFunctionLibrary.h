// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "MyBlueprintFunctionLibrary.generated.h"

/**
 * 
 */
UCLASS()
class AIEXERCICE_API UMyBlueprintFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

		UFUNCTION(BlueprintCallable , Category = "Custom Message")
		static void Print(FString message);
	
		UFUNCTION(BlueprintCallable , Category = "Custom Light")
		static void ToggleAllLights();
	
		UFUNCTION(BlueprintCallable , Category = "MaterialB")
		static void SetMaterialInstanceStaticSwitchParameterValue(
			UMaterialInstance* Instance, FName ParamaterName, bool value);
};
