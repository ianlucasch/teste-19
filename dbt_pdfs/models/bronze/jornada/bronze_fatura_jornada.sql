WITH formatted AS (
    SELECT
        CAST("n_nota" AS INT) AS n_nota,
        "cv",
        "merc",
        "tipo",
        TO_DATE("vecto", 'DDMMYYYY') AS vecto,
        CAST("qted" AS INT) AS qted,
        "mercadoria",
        CAST(REPLACE("cotacao", ',', '.') AS DECIMAL(10, 2)) AS cotacao,
        TO_DATE("data_de_pregao", 'DDMMYYYY') AS data_de_pregao,
        CAST(REPLACE("txop", ',', '.') AS DECIMAL(10, 2)) AS txop
    FROM
        {{ source('automacao_pdfs', 'fatura_jornada') }}
)

SELECT * 
FROM formatted