# criando o navegador sincrono
from playwright.sync_api import sync_playwright

# importando uma biblioteca time (controle de tempo)
import time

webpages = ["nike.com", "globo.com"]
infowebpages = {}

# aqui eu defino em qual navegador eu vou utilizar e fazer os testes
# ele está rodando esse comando sync_playwright() e está armazenando essa resposta do playwright dentro da letra p, e a palavra with está garanindo que ele vai abrir e fechar o processo automaticamente
with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # o playwright() cria o navegador no módulo headless, ou seja, sem o navegador aparecer
    
    # criando uma página dentro do meu navegador e armazenando em ma variavel
    browserpage = browser.new_page()

    for x in webpages:
        # informando o site que eu quero que o playwright() navegue
        browserpage.goto(f"https://www.spyfu.com/overview/domain?query={x}")

        browserpage.locator('xpath=//*[@id="app"]/div[1]/nav/div[1]/div/div/div[2]/a').click()
        time.sleep(10)

        organickeywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/a/div[2]').text_content()
        organickeywordsnew = {}
        organickeywordsnew["Organic Keywords"] = organickeywords

        sumofrankchance = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[2]/a/div[2]/div').text_content()
        sumofrankchancenew = {}
        sumofrankchancenew["Sum of Rank Change"] = sumofrankchance

        estmonthlyseoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/a/div[2]').text_content()
        estmonthlyseoclicksnew = {}
        estmonthlyseoclicksnew["Est Monthly Seo Clicks"] = estmonthlyseoclicks
        
        estmoseoclicksvalue = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[4]/a/div[2]').text_content()
        estmoseoclicksvaluenew = {}
        estmoseoclicksvaluenew["Est Mo Seo Clicks Value"] = estmoseoclicksvalue
        
        page1keywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/a').text_content()
        almostthere = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/a').text_content()
        almosttherehank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/span').text_content()
        pagesto = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/a').text_content()
        pagestorank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div[2]/div[2]').text_content()
        yearsmos = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div/div/div[1]/div/a/div[1]/div/div').text_content()
        keywordstheirtop2 = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div/div/div[2]/div/a/div[1]/div[2]').text_content()
        
        browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/h2').click()
        time.sleep(5)

        toporganiccompetitors1 = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[1]').text_content()
        toporganiccompetitors2 = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[2]').text_content()
        toporganiccompetitors3 = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[3]').text_content()
        toporganiccompetitors4 = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[4]').text_content()
        toporganiccompetitors5 = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[5]').text_content()
        toporganiccompetitors = {"Top Organic Competitors":
                                    {
                                        "1": toporganiccompetitors1, 
                                        "2": toporganiccompetitors2, 
                                        "3": toporganiccompetitors3, 
                                        "4": toporganiccompetitors4, 
                                        "5": toporganiccompetitors5,
                                    }
                                }

        browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/h2').click()
        time.sleep(5)

        mostvaluablekeywords1keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[1]/td[1]').text_content()
        mostvaluablekeywords1seocliks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[1]/td[2]').text_content()
        mostvaluablekeywords1volume = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]').text_content()
        mostvaluablekeywords1 = {"TOP 1": 
                                    {"Keyword": mostvaluablekeywords1keyword, 
                                    "SEO Clicks": mostvaluablekeywords1seocliks, 
                                    "Volume": mostvaluablekeywords1volume
                                    }
                                }
    
        mostvaluablekeywords2keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[1]').text_content()
        mostvaluablekeywords2seocliks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[2]').text_content()
        mostvaluablekeywords2volume = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[3]').text_content()
        mostvaluablekeywords2 = {"TOP 2": 
                                    {"Keyword": mostvaluablekeywords2keyword, 
                                    "SEO Clicks": mostvaluablekeywords2seocliks, 
                                    "Volume": mostvaluablekeywords2volume
                                    }
                                }
        
        mostvaluablekeywords3keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[3]/td[1]').text_content()
        mostvaluablekeywords3seocliks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[3]/td[2]').text_content()
        mostvaluablekeywords3volume = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[3]/td[3]').text_content()
        mostvaluablekeywords3 = {"TOP 3": 
                                    {"Keyword": mostvaluablekeywords3keyword, 
                                    "SEO Clicks": mostvaluablekeywords3seocliks, 
                                    "Volume": mostvaluablekeywords3volume
                                    }
                                }
        
        mostvaluablekeywords4keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[4]/td[1]').text_content()
        mostvaluablekeywords4seocliks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[4]/td[2]').text_content()
        mostvaluablekeywords4volume = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[4]/td[3]').text_content()
        mostvaluablekeywords4 = {"TOP 4": 
                                    {"Keyword": mostvaluablekeywords4keyword, 
                                    "SEO Clicks": mostvaluablekeywords4seocliks, 
                                    "Volume": mostvaluablekeywords4volume
                                    }
                                }
        
        mostvaluablekeywords5keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[5]/td[1]').text_content()
        mostvaluablekeywords5seocliks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[5]/td[2]').text_content()
        mostvaluablekeywords5volume = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr[5]/td[3]').text_content()
        mostvaluablekeywords5 = {"TOP 5": 
                                    {"Keyword": mostvaluablekeywords5keyword, 
                                    "SEO Clicks": mostvaluablekeywords5seocliks, 
                                    "Volume": mostvaluablekeywords5volume
                                    }
                                }

        mostvaluablekeywordstop5 = {}
        mostvaluablekeywordstop5["Most Valuable Keywords"] = mostvaluablekeywords1, mostvaluablekeywords2, mostvaluablekeywords3, mostvaluablekeywords4, mostvaluablekeywords5
        
        newlyrankedkeywords1keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]').text_content()
        newlyrankedkeywords1rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div/div/span[1]').text_content()
        newlyrankedkeywords1seoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]').text_content()
        newlyrankedkeywords1 = {"TOP 1":
                                    {"Keyword": newlyrankedkeywords1keyword,
                                    "Rank": newlyrankedkeywords1rank,
                                    "SEO Cliks": newlyrankedkeywords1seoclicks
                                    }
                            }
        
        newlyrankedkeywords2keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]').text_content()
        newlyrankedkeywords2rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div/div/span[1]').text_content()
        newlyrankedkeywords2seoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[2]/td[3]').text_content()
        newlyrankedkeywords2 = {"TOP 2":
                                    {"Keyword": newlyrankedkeywords2keyword,
                                    "Rank": newlyrankedkeywords2rank,
                                    "SEO Cliks": newlyrankedkeywords2seoclicks
                                    }
                            }
        
        newlyrankedkeywords3keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[3]/td[1]').text_content()
        newlyrankedkeywords3rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[3]/td[2]/div/div/span[1]').text_content()
        newlyrankedkeywords3seoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[3]/td[3]').text_content()
        newlyrankedkeywords3 = {"TOP 3":
                                    {"Keyword": newlyrankedkeywords3keyword,
                                    "Rank": newlyrankedkeywords3rank,
                                    "SEO Cliks": newlyrankedkeywords3seoclicks
                                    }
                            }
        
        newlyrankedkeywords4keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[1]').text_content()
        newlyrankedkeywords4rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[2]/div/div/span[1]').text_content()
        newlyrankedkeywords4seoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[3]').text_content()
        newlyrankedkeywords4 = {"TOP 4":
                                    {"Keyword": newlyrankedkeywords4keyword,
                                    "Rank": newlyrankedkeywords4rank,
                                    "SEO Cliks": newlyrankedkeywords4seoclicks
                                    }
                            }
        
        newlyrankedkeywords5keyword = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[1]').text_content()
        newlyrankedkeywords5rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[2]/div/div/span[1]').text_content()
        newlyrankedkeywords5seoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[2]/div/div/div/table/tbody/tr[4]/td[3]').text_content()
        newlyrankedkeywords5 = {"TOP 5":
                                    {"Keyword": newlyrankedkeywords5keyword,
                                    "Rank": newlyrankedkeywords5rank,
                                    "SEO Cliks": newlyrankedkeywords5seoclicks
                                    }
                            }

        newlyrankedkeywordstop5 = {}
        newlyrankedkeywordstop5["Newly Ranked Keywords"] = newlyrankedkeywords1, newlyrankedkeywords2, newlyrankedkeywords3, newlyrankedkeywords4, newlyrankedkeywords5
        
        browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/h2').click()
        time.sleep(5)

        pageonekeywords1keywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[1]/td[1]').text_content()
        pageonekeywords1rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[1]/td[2]').text_content()
        pageonekeywords1 = {"TOP 1":
                                {
                                    "Keyword": pageonekeywords1keywords,
                                    "Rank(Change)": pageonekeywords1rank
                                }
                        }

        pageonekeywords2keywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[1]').text_content()
        pageonekeywords2rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[2]/td[2]').text_content()
        pageonekeywords2 = {"TOP 2":
                                {
                                    "Keyword": pageonekeywords2keywords,
                                    "Rank(Change)": pageonekeywords2rank
                                }
                        }

        pageonekeywords3keywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[3]/td[1]').text_content()
        pageonekeywords3rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[3]/td[2]').text_content()
        pageonekeywords3 = {"TOP 3":
                                {
                                    "Keyword": pageonekeywords3keywords,
                                    "Rank(Change)": pageonekeywords3rank
                                }
                        }

        pageonekeywords4keywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[4]/td[1]').text_content()
        pageonekeywords4rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[4]/td[2]').text_content()
        pageonekeywords4 = {"TOP 4":
                                {
                                    "Keyword": pageonekeywords4keywords,
                                    "Rank(Change)": pageonekeywords4rank
                                }
                        }

        pageonekeywords5keywords = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[5]/td[1]').text_content()
        pageonekeywords5rank = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div/div/div/table/tbody/tr[5]/td[2]').text_content()
        pageonekeywords5 = {"TOP 5":
                                {
                                    "Keyword": pageonekeywords5keywords,
                                    "Rank(Change)": pageonekeywords5rank
                                }
                        }
        
        pageonekeywordstop5 = {}
        pageonekeywordstop5["Page One Keywords"] = pageonekeywords1, pageonekeywords2, pageonekeywords3, pageonekeywords4, pageonekeywords5
        
        browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/h2').click()
        time.sleep(7)

        toppages1page = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]/div').text_content()
        toppages1estmonthlyseoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]').text_content()
        toppages1 = {"TOP 1":
                        {
                            "Page": toppages1page,
                            "Est Monthly SEO Clicks": toppages1estmonthlyseoclicks,
                        }                    
                    }

        toppages2page = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[1]/div').text_content()
        toppages2estmonthlyseoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[2]').text_content()
        toppages2 = {"TOP 2":
                        {
                            "Page": toppages2page,
                            "Est Monthly SEO Clicks": toppages2estmonthlyseoclicks,
                        }                    
                    }

        toppages3page = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[5]/td[1]/div').text_content()
        toppages3estmonthlyseoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[5]/td[2]').text_content()
        toppages3 = {"TOP 3":
                        {
                            "Page": toppages3page,
                            "Est Monthly SEO Clicks": toppages3estmonthlyseoclicks,
                        }                    
                    }

        toppages4page = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[7]/td[1]/div').text_content()
        toppages4estmonthlyseoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[7]/td[2]').text_content()
        toppages4 = {"TOP 4":
                        {
                            "Page": toppages4page,
                            "Est Monthly SEO Clicks": toppages4estmonthlyseoclicks,
                        }                    
                    }

        toppages5page = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[9]/td[1]/div').text_content()
        toppages5estmonthlyseoclicks = browserpage.locator('xpath=//*[@id="app"]/main/div/div/main/div/div/div/div[2]/div[2]/div[5]/div/div/div/div/div[1]/div/div[1]/table/tbody/tr[9]/td[2]').text_content()
        toppages5 = {"TOP 5":
                        {
                            "Page": toppages5page,
                            "Est Monthly SEO Clicks": toppages5estmonthlyseoclicks,
                        }                    
                    }

        toppagestop5 = {}
        toppagestop5["Top Pages"] = toppages1, toppages2, toppages3, toppages4, toppages5

        infowebpages[x] = (organickeywordsnew, sumofrankchancenew, estmonthlyseoclicksnew, estmoseoclicksvaluenew, page1keywords, 
                           almostthere + almosttherehank, pagesto + pagestorank, yearsmos, keywordstheirtop2, toporganiccompetitors, 
                           mostvaluablekeywordstop5, newlyrankedkeywordstop5, pageonekeywordstop5, toppagestop5)


print(infowebpages)
