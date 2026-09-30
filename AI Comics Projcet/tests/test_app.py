* {
    box-sizing: border-box;
}


body {

    margin: 0;

    font-family:
        Inter,
        system-ui,
        Arial,
        sans-serif;

    background: #f4f5f8;

    color: #1f2937;
}


.site-header {

    background: #171717;

    color: white;

    padding: 18px 6%;

    display: flex;

    justify-content: space-between;

    align-items: center;
}


.brand {

    color: white;

    text-decoration: none;

    font-size: 1.25rem;

    font-weight: 800;
}


.container {

    max-width: 1100px;

    margin: auto;

    padding: 40px 20px;
}


.hero {

    text-align: center;

    max-width: 800px;

    margin:
        20px auto
        35px;
}


.hero h1 {

    font-size:
        clamp(
            2rem,
            5vw,
            4rem
        );

    margin-bottom: 12px;
}


.hero p {

    color: #5b6472;

    font-size: 1.1rem;
}


.card {

    background: white;

    border-radius: 18px;

    padding: 24px;

    box-shadow:
        0 10px 30px
        rgba(0, 0, 0, 0.06);

    margin-bottom: 24px;
}


.form-grid {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 18px;
}


.full {

    grid-column:
        1 / -1;
}


label {

    display: flex;

    flex-direction: column;

    gap: 8px;

    font-weight: 700;
}


input,
textarea,
select {

    font: inherit;

    padding: 13px;

    border:
        1px solid #d5d9df;

    border-radius: 10px;

    background: white;
}


textarea {

    min-height: 140px;

    resize: vertical;
}


button,
.button {

    border: none;

    border-radius: 10px;

    padding:
        12px 18px;

    font-weight: 800;

    text-decoration: none;

    cursor: pointer;

    display: inline-block;
}


.primary {

    background: #111827;

    color: white;
}


.secondary {

    background: #e5e7eb;

    color: #111827;
}


.alert {

    background: #fee2e2;

    color: #991b1b;

    padding: 15px;

    border-radius: 10px;

    margin-bottom: 20px;
}


.tip {

    color: #596273;

    font-size: 0.95rem;
}


.page-head {

    display: flex;

    justify-content: space-between;

    align-items: center;

    gap: 20px;

    margin-bottom: 20px;
}


.comic-grid {

    display: grid;

    gap: 24px;
}


.panel img {

    display: block;

    width: 100%;

    max-height: 650px;

    object-fit: cover;

    border-radius: 12px;

    border:
        1px solid #ddd;
}


.scene {

    color: #596273;
}


.center {

    text-align: center;
}


.test-image {

    max-width: 100%;

    border-radius: 12px;
}


footer {

    text-align: center;

    color: #697386;

    padding: 30px;
}


@media (max-width: 700px) {

    .form-grid {

        grid-template-columns: 1fr;

    }


    .full {

        grid-column: auto;

    }


    .page-head {

        flex-direction: column;

        align-items: flex-start;

    }


    .site-header {

        flex-direction: column;

        align-items: flex-start;

        gap: 10px;

    }

}