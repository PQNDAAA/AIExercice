#pragma once

#include "CoreMinimal.h"
#include "UObject/ObjectMacros.h"
#include "Engine/DataTable.h"
#include "enu.h"
#include "Microsoft/AllowMicrosoftPlatformTypes.h"
#include "StructTest.generated.h"

USTRUCT(BlueprintType)
struct FStructTest : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()

public:
	
	// Propriétés de la DataRow
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "MyDataRow")
	FString Name;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "MyDataRow")
	Eenu myenum;
	
	// Constructeur par défaut
	FStructTest() {}
};
