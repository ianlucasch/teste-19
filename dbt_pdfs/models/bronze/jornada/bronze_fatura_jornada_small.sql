WITH formatted AS (
    SELECT
        CAST("n_nota" AS INT) AS n_nota,
        TO_DATE("data_de_pregao", 'DDMMYYYY') AS data_de_pregao,
        CAST(REPLACE("corretagem", ',', '.') AS DECIMAL(10, 2)) AS tx_corretagem,
        CAST(REPLACE("taxa_de_registro", ',', '.') AS DECIMAL(10, 2)) AS taxa
    FROM
        {{ source('automacao_pdfs', 'fatura_jornada_small') }}
)

SELECT * 
FROM formatted