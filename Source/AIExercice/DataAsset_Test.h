// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "DataAsset_Test.generated.h"

USTRUCT()
struct FItemInfo {

    GENERATED_USTRUCT_BODY()

        UPROPERTY(EditAnywhere)
        FString itemName;

    UPROPERTY(EditAnywhere)
        int villagersMax;

    UPROPERTY(EditAnywhere)
        UBlueprint* itemBlueprint;

    UPROPERTY(EditAnywhere)
        FColor itemColor;
};


UCLASS(BlueprintType)
class AIEXERCICE_API UDataAsset_Test : public UDataAsset
{
	GENERATED_BODY()
        UPROPERTY(EditAnywhere)
        TArray<FItemInfo> items;
};
